<template>
    <div class="container">
    <input class="input" type="text" v-model="value" placeholder="Search" ref="input" @blur="onBlur">
    <div class="results">
        <div class="result" v-for="result in results" :key="result.id || result.text" @click="selectResult(result)">
            <slot v-bind:result="result">
                {{result.text}}
            </slot>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    props: {
        values: { type: Array, required: true },
        focus: { type: Boolean, default: false }
    },
    data() {
        return {
            value: '',
            words: [],
            result: ''
        }
    },
    computed: {
        wordsDict() {
            const res = {}
            this.values.forEach(v => {
                v && v.text &&
                v.text.split(' ').forEach(w => {
                    const word = w.toLowerCase()
                    res[word] = res[word] || []
                    res[word].push(v)
                })
            })
            return res
        },
        results() {
            const words = Object.keys(this.wordsDict);
            return this.value ? words.filter(w => w.startsWith(this.value)).reduce((res,w) => { res.push(...this.wordsDict[w].filter(v => res.indexOf(v)<0)); return res},[]) : []
        }
    }, 

    methods: {
        selectResult(result) {
            this.$emit("change", {...result})
            this.result = result
            this.value = ''
        },
        focusInput() {
            this.$refs.input.focus()
        },
        onBlur() {
            setTimeout(() => !this.result && this.$emit("cancel"), 500)
        }
    },
    mounted() {
        if (this.focus) this.focusInput()
    }
}
</script>

<style scoped>
    .results {
        max-height: 300px;
        overflow: auto;
        border: 1px solid black;
        position: absolute;
        width: 100%;
        background: white;
    }

    .result {
        min-height: 48px;
    }

    .result:hover {
        background: rgb(4, 65, 65);
        color: white;

    }

    .container {
        position: relative;
    }

    .input {
        width: 100%;
    }
</style>