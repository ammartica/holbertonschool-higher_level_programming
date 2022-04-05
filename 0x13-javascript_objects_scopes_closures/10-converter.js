#!/usr/bin/node
// Converts number from base 10 to another base passed as argument

exports.converter = function (base) {
  return function myConverter (n) {
    return n.toString(base);
  };
};
