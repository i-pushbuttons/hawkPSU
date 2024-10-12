const { getDataConnect, validateArgs } = require('firebase/data-connect');

const connectorConfig = {
  connector: 'default',
  service: 'comp_stem',
  location: 'us-central1'
};
exports.connectorConfig = connectorConfig;

