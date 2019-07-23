import Vue from "vue";
import Axios from "axios";
import store from "./store";
import router from "./router";
import App from "./App.vue"


Vue.config.productionTip = process.env.NODE_ENV === "development";

Axios.interceptors.response.use(function (response) {
	return response;
}, function (error) {
	if (error.response.status === 404) {
		router.push({name: "error_404"});
	}
	return Promise.reject(error);
});

new Vue({
	router,
	store,
	data(){return {}},
	render: h => h(App),
}).$mount("#app");
