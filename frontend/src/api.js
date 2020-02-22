window.state = {};

export default {
    async login(email, pass) {
        var body = {
            email,
            password: pass
        }
        state.$global.waiting = true;
        try {
            var res = await fetch(
                '/api/login', {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json;charset=UTF-8'
                },
                body: JSON.stringify(body),
                method: 'POST'
            })

            if (res.ok) {
                var token = await res.text()
                localStorage.setItem('api-token', token)
                state.$global.loggedIn = true
            } else {
                throw new Error(`Unable to login:  ${res.statusText} (${res.status})`)
            }
        } finally {
            state.$global.waiting = false;
        }
    },
    logout() {
        localStorage.removeItem('api-token')
        state.$global.loggedIn = false
    },
    async get(type, id) {
        var res = await fetch(
            '/api/' + type, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': localStorage.getItem('api-token')
            },
        })
        if (res.ok) {
            return res.json()
        } else {
            // todo: handle auth errors
            throw new Error(`${res.status} (${res.statusText})`)
        }
    },
    setup(vm) {
        state = vm;
        var cachedToken = localStorage.getItem('api-token')
        if (cachedToken) {
            state.$global.loggedIn = true;
        }
    }
}
