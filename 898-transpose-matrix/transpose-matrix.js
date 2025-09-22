/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    const row = matrix.length
    const col = matrix[0].length

    let matrix2 = Array.from({ length: col }, () => Array(row).fill(0));

    for (let i = 0; i< row; i++){
        for(let j = 0; j< col; j++){
            matrix2[j][i] = matrix[i][j]
        }
    }

    return matrix2 


};