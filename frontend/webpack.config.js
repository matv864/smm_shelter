const path = require('path');

module.exports = {
  entry: './src/App.js',
  module: {
    rules: [
      { test: /\.svg$/, use: 'svg-inline-loader' },
      { test: /\.css$/, use: [ 'style-loader', 'css-loader' ] },
      { test: /\.(js)$/, use: 'babel-loader' }
    ]
  },
  output: {
    path: path.resolve(__dirname, '/app/dist'),
    filename: 'bundle.js',
  },
  mode: process.env.NODE_ENV === 'production' ? 'production' : 'development'
};