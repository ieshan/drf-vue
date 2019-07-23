process.env.NODE_ENV = typeof process.env.NODE_ENV === "undefined" ? "development" : process.env.NODE_ENV;

const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");
const config = require("./frontend.config");

const staticDir = __dirname + "/backend/frontend/static/frontend";
const PORT = 8201;

module.exports = {
	publicPath: config.publicPath,
	outputDir: staticDir + "/frontend-bundle/",
	configureWebpack: {
		entry: {
			app: path.resolve(__dirname, "./frontend/main.js")
		},
		devServer: {
			host: "localhost",
			port: PORT,
			disableHostCheck: true,

			headers: {
				"Access-Control-Allow-Origin": "*",
				"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
				"Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
			},
			useLocalIp: false,
		},
		plugins: [
			new BundleTracker({
				path: __dirname,
				filename: "./frontend-stats.json"
			})
		],
		resolve: {
			alias: {
				"@": __dirname + "/frontend"
			}
		}
	},
	chainWebpack: config => {
		//config.entry("app").clear().add(path.resolve(__dirname, "./website/main.js")).add(path.resolve(__dirname, "./website/scss/style.scss")).end();
		//config.optimization.splitChunks(false);
	}
};
