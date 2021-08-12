module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://backend:8000/:path*",
      },
    ];
  },
  webpackDevMiddleware: config => {
    config.watchOptions = {
      poll: 800,
      aggregateTimeout: 300,
    }
    return config
  },
};