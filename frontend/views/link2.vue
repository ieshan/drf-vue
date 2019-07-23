<template>
	<div class="row">
		<div class="col">
			<h1>Link 2</h1>
			<p>{{data}}</p>
		</div>
	</div>
</template>

<script>
	import Axios from "axios";
	export default {
		name: "link2",
		data() {
			return {
				data: ""
			}
		},
		created() {
			let self = this;
			Axios.get("api/v1/frontend/dummy/").then(function (res) {
				self.data = res.data.data;
			}).catch(function (err) {
				console.log(err);
			})
		}
	}
</script>
