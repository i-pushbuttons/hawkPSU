// eslint.config.js
const googleConfig = require('eslint-config-google');

module.exports = [
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      globals: {
        es6: true,
        node: true,
      },
    },
    rules: {
      'no-restricted-globals': ['error', 'name', 'length'],
      'prefer-arrow-callback': 'error',
      'quotes': ['error', 'single', {allowTemplateLiterals: true}],
      // Ensure 'valid-jsdoc' rule is removed
    },
  },
  {
    files: ['**/*.spec.*'],
    languageOptions: {
      globals: {
        mocha: true,
      },
    },
    rules: {},
  },
  {
    files: ['**/*.js'],
    ...googleConfig,
    rules: {
      ...googleConfig.rules,
      // Ensure 'valid-jsdoc' rule is removed
    },
  },
];

