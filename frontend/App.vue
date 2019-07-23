<template>
	<div>
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			<router-link :to="{name: 'home'}" class="navbar-brand" >
				Brand
			</router-link>

			<div class="collapse navbar-collapse">
				<ul class="navbar-nav mr-auto">
					<router-link :to="{name: 'link1'}" class="nav-item" tag="li" active-class="active">
						<a class="nav-link">Link 1</a>
					</router-link>
					<router-link :to="{name: 'link2'}" class="nav-item" tag="li" active-class="active">
						<a class="nav-link">Link 2</a>
					</router-link>
				</ul>
			</div>
		</nav>

		<div class="container">
			<router-view/>
		</div>
	</div>
</template>

<script>
	export default {
		name: "app",
		data() {
			return {}
		}
	}
</script>
