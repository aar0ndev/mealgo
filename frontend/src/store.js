
var _id = 0
function nextId () {
  return _id++
}

async function sleep (seconds) {
  return new Promise((resolve, reject) => setTimeout(() => resolve(), seconds * 1000))
}

async function tryAdd (vm, actionObject) {
  // if offline, register for sync when online
  if (!vm.online) {
    vm.pendingActions.push(actionObject)
    await vm.waitUntilOnline()
    vm.pendingActions = vm.pendingActions.filter(a => a.pendingId !== actionObject.pendingId)
  }

  var res = null
  // otherwise try to resolve the action by sync with backend
  try {
    res = await vm.$api.add(actionObject.type, actionObject.data)
  } catch (err) {
    // handle auth errors, server errors (404, 500, etc)
    actionObject.retries = (actionObject.retries || 0) + 1
    // if retries exceeds maxRetries, raise error
    if (actionObject.retries >= actionObject.maxRetries) {
      throw actionObject.err || new Error('max retries exceeded')
    }
    await sleep(0.2)
    await tryAdd(vm, actionObject)
  }
  return res
}

export default {
  data () {
    return {
      pendingActions: [],
      meals: [],
      mode: 'online'
    }
  },
  watch: {
    pendingActions () {
      localStorage.setItem('store_pendingActions', JSON.stringify([...this.pendingActions]))
    }
  },
  methods: {
    addMeal (meal) {
      this.meals = [...this.meals, meal]
      var pendingAction = { type: 'meal', data: meal, action: 'add', added: new Date(), pendingId: nextId(), maxRetries: 3 }
      return tryAdd(this, pendingAction)
    },
    async waitUntilOnline () {
      while (true) {
        if (this.mode === 'online') { return }
        await sleep(0.2)
      }
    }
  },
  mounted () {
    this.pendingActions = JSON.parse(localStorage.getItem('store_pendingActions'))
    for (var action in this.pendingActions) {
      console.log('pending action', action)
    }
  }
}
// add item to store, store attempts from API (handles retries, offline/online events, backend errors)
