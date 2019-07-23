import Vue from "vue";
import Router from "vue-router"

import Home from "./views/home";
import Link1 from "./views/link1";
import Link2 from "./views/link2";

Vue.use(Router);
let router = new Router({
	base: "/",
	mode: "hash",
	linkActiveClass: "active",
	routes: [
		{
			path: "/",
			name: "redirect",
			component: {
				render: h => h(),
				created: function() {
					this.$router.push({name: "home"});
				}
			}
		},
		{
			path: "/home",
			component: Home,
			name: "home"
		},
		{
			path: "/link1",
			component: Link1,
			name: "link1"
		},
		{
			path: "/link2",
			component: Link2,
			name: "link2"
		},
	]
});

export default router;
