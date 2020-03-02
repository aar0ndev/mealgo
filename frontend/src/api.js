var state = {}
window.state = state
const API_TOKEN_KEY = '6de43cb1-994e-497a-bfeb-768ba96fa875'

// provide implementation independent abstraction over api requests
async function request (url, method = 'GET', body = null, headers = {}, wait = true) {
  if (wait) {
    state.$global.waiting = true
  }
  try {
    var opts = {
      headers: {
        'Authentication-Token': localStorage.getItem(API_TOKEN_KEY),
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        ...headers
      },

      method
    }

    if (method === 'POST' || method === 'PATCH') {
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
      var { token } = await request('/api/login', 'POST', body)
      localStorage.setItem(API_TOKEN_KEY, token)
      state.$global.loggedIn = true
    } catch (err) {
      throw new Error(`Unable to login:  ${err.res.statusText} (${err.res.status})`)
    }
  },
  logout () {
    localStorage.removeItem(API_TOKEN_KEY)
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
  async add (type, body) {
    // debugger
    try {
      var res = await request(`/api/${type}`, 'POST', body)
      return res
    } catch (err) {
      // todo: handle auth errors
      throw new Error(`${err.res.status} (${err.res.statusText})`)
    }
  },
  async delete (type, id) {
    // debugger
    try {
      var res = await request(`/api/${type}/${id}`, 'DELETE', null)
      return res
    } catch (err) {
      // todo: handle auth errors
      throw new Error(`${err.res.status} (${err.res.statusText})`)
    }
  },
  async update (type, id, body) {
    // debugger
    try {
      var res = await request(`/api/${type}/${id}`, 'PATCH', body)
      return res
    } catch (err) {
      // todo: handle auth errors
      throw new Error(`${err.res.status} (${err.res.statusText})`)
    }
  },
  setup (vm) {
    state = vm
    var cachedToken = localStorage.getItem(API_TOKEN_KEY)
    if (cachedToken) {
      state.$global.loggedIn = true
    }
    return vm
  }
}
