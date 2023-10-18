/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    config.externals.push({
      'utf-8-validate': 'commonjs utf-8-validate',
      'bufferutil': 'commonjs bufferutil',
    })
    return config
  },
  reactStrictMode: false,
  trailingSlash: true,
  // productionBrowserSourceMaps: true,
  images: {}
};

module.exports = nextConfig
