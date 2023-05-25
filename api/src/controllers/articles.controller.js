const model = require('../models/articles.model')

async function searchArticlesByKeywords(req, res) {
  const { keywords } = req.query;

  try {
    // Query articles in BigQuery matching the keywords
    const articles = await model.searchArticlesByKeywords(keywords);
    res.status(200).json(articles);

  } catch (error) {
    console.error('Error searching articles:', error);
    res.status(500).json({ message: 'An error occurred while searching articles', error });
  }
};

module.exports = {
  searchArticlesByKeywords,
}
