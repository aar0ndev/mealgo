var state = {}
window.state = state

// provide implementation independent abstraction over api requests
async function request (url, body = null, method = 'GET', headers = {}, wait = true) {
  if (wait) {
    state.$global.waiting = true
  }
  try {
    var opts = {
      headers: {
        'Authorization': localStorage.getItem('api-token'),
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        ...headers
      },

      method
    }

    if (method === 'POST') {
      opts.body = JSON.stringify(body)
    }

    var res = await fetch(url, opts)

    if (res.ok) {
      return res.json()
    } else {
      var err = new Error(`${res.statusText} (${res.status})`)
      err.res = res
      throw err
    }
  } finally {
    if (wait) {
      state.$global.waiting = false
    }
  }
}

export default {
  async login (email, pass) {
    var body = {
      email,
      password: pass
    }

    try {
      var { token } = await request('/api/login', body, 'POST')
      localStorage.setItem('api-token', token)
      state.$global.loggedIn = true
    } catch (err) {
      throw new Error(`Unable to login:  ${err.res.statusText} (${err.res.status})`)
    }
  },
  logout () {
    localStorage.removeItem('api-token')
    state.$global.loggedIn = false
  },
  async get (type, id = null) {
    // debugger
    try {
      var res = await request(`/api/${type}` + (id ? `/${id}` : ''))
      return res
    } catch (err) {
      // todo: handle auth errors
      throw new Error(`${err.res.status} (${err.res.statusText})`)
    }
  },
  setup (vm) {
    state = vm
    var cachedToken = localStorage.getItem('api-token')
    if (cachedToken) {
      state.$global.loggedIn = true
    }
  }
}
