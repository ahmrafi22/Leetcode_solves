/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const result = []
    const maxLen = Math.max(word1.length, word2.length)

    for (let i =0; i < maxLen; i++){
         i < word1.length &&  result.push(word1[i]) ;
         i < word2.length &&  result.push(word2[i]) ;
    }

    return result.join('')
};