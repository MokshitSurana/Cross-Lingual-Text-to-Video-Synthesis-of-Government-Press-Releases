/** @type {import('tailwindcss').Config} */
const tailwind = {
  darkMode: ['class'],
  // purge: ['./src/**/*.{js,ts,jsx,tsx}', "./pages/**/*.{js,ts,jsx,tsx}"],
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './layouts/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    container: {
      center: true,
      screens: {
        lg: '960px',
        xl: '1140px',
        '2xl': '1200px',
      },
      padding: '15px'
    },
    typography: (theme) => ({}),
    extend: {
      boxShadow: {
        'inset':'inset 0px 0px 19px -8px rgba(0,0,0,0.2);',
      },
    },
  },
  variants: {},
  plugins: [require('@tailwindcss/typography')],
}

module.exports = tailwind