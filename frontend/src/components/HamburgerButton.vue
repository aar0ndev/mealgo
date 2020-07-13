 <template>
    <button>
        <div></div>
        <div></div>
        <div></div>
    </button>
</template>

<style scoped>
    button {
        border: none;
        background: none;
    }
    div {
        width: 35px;
        height: 3px;
        opacity: 0.5;
        background-color: black;
        margin: 6px 0;
    }
    button:hover div, button:focus div {
        background-color: black;
        opacity: 1;
    }
</style>
