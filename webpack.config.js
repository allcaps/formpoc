const path = require("path");
const webpack = require("webpack");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');

const source = path.resolve(path.join("./webapp", "./static_src"));
const destination = path.resolve(path.join("./webapp", "./static"));

const config = {
  entry: {
    main: [
      path.join(source, "js", "main.js"),
      path.join(source, "scss", "main.scss"),
    ],
  },
  output: {
    path: destination,
    publicPath: "",
    filename: "[name]-[fullhash].js",
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        }
      },
      {
        test: /\.(scss|css)$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
            },
          },
          {
            loader: "postcss-loader",
            options: {
              sourceMap: true,
              postcssOptions: {
                plugins: [
                  "postcss-preset-env"
                ]
              }
            },
          },
          "sass-loader",
        ],
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        use: [
          {
            loader: "file-loader",
            options: {
              outputPath: "fonts/",
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: "[name]-[fullhash].css",
    }),
    new WebpackManifestPlugin(),
  ],
};

module.exports = (env, argv) => {
  if (argv.mode === "development") {
    config.devtool = "inline-source-map";
  }
  return config;
};
