module.exports = {
  root: true,
  env: {
    es6: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'google',
  ],
  rules: {
    'quotes': ['error', 'single'],
    'require-jsdoc': 'off', // Turn off the deprecated rule
  },
  parserOptions: {
    ecmaVersion: 2018,
  },
};
