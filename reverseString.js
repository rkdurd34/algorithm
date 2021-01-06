a = "hello"
b = 'abcdefg'
function sol(word){
  const wordList = word.split("")
  let revisedList = []
  for (let i =  wordList.length; i > -1 ; i--){
    revisedList.push(word[i])
  }
  return revisedList.join('')
};
c = sol(a)
console.log(c)

