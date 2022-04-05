#!/usr/bin/node
// Returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const element of list) {
    if (element === searchElement) {
      total++;
    }
  }
  return total;
};
