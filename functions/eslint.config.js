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
      'require-jsdoc': 'off', // Turn off the deprecated rule
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
      'require-jsdoc': 'off', // Turn off the deprecated rule
      'valid-jsdoc': 'off', // Turn off the deprecated valid-jsdoc rule
    },
  },
];
