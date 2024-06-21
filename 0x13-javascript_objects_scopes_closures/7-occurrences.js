exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => count + (element === searchElement ? 1 : 0), 0);
};
exports.esrever = function (list) {
    const reversedList = [];
    for (let i = list.length - 1; i >= 0; i--) {
      reversedList.push(list[i]);
    }
    return reversedList;
  };
  