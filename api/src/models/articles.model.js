const { BigQuery } = require('@google-cloud/bigquery');
const path = require('path');

// Configure Google Cloud BigQuery with the service account key file path
const currentDir = path.dirname(__filename);
const credentialsPath = path.join(currentDir, '..', '..', '..', 'crawler', 'src', 'credentials', 'sa_gbq_crawler_credentials.json');

const bigquery = new BigQuery({ keyFilename: credentialsPath });

async function searchArticlesByKeywords(keywords) {
  const query = `
    SELECT *
    FROM lima-technical-challenge.crawler.bbc_news
    WHERE LOWER(headline) LIKE '%${keywords.toLowerCase()}%'
      OR LOWER(subtitle) LIKE '%${keywords.toLowerCase()}%'
      OR LOWER(text) LIKE '%${keywords.toLowerCase()}%'
  `;

  const [rows] = await bigquery.query(query);

  return rows;
}

module.exports = {
  searchArticlesByKeywords,
}
