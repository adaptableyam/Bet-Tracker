/** @type {import('tailwindcss').Config} */


module.exports = {
  content: ["./tracker/**/*.{html,js}"],
  theme: {

    extend: {},
  },
  plugins: [
  require('@tailwindcss/forms'),
  require('@tailwindcss/typography'),
  ],
  safelist: [
    'focus:ring-1',
    'focus:border-indigo-500',
    'focus:outline-none',
    'focus:ring-indigo-500',
    'focus:ring-offset-0',
    'focus:ring-white',
    'text-indigo-500',
  ],
}

