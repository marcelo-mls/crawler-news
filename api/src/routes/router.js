const express = require('express');
const controller = require('../controllers/articles.controller')

const router = express.Router();

// http://localhost:3001/articles?keywords=
router.get('/articles', controller.searchArticlesByKeywords)

module.exports = router;
