// Create a webpage which will ask the user for an unput and determines whether that input was a palindrome or not.

function isPalindrome() {
  var inputWord = document.getElementById("inputWord").value.toLowerCase();
  var reverseWord = [];

  for (var i = 0; i < inputWord.length; i++) {
    reverseWord.unshift(inputWord[i]);
  }
  reverseWord = reverseWord.join('');
  if (reverseWord == inputWord) {
    console.log(true);
    document.getElementById("result").innerHTML = inputWord + " is a palindrome."
  } else {
    console.log(false);
    document.getElementById("result").innerHTML = inputWord + " is not palindrome."
  }
};

var checkForPalindromeButton = document.getElementById('checkForPalindromeButton');
console.log(checkForPalindromeButton)

checkForPalindromeButton.addEventListener('click',isPalindrome);
