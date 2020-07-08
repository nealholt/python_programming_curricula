import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class Hangman {

	//Only 6 mistakes are allowed until the user loses.
	private static final int LOSE_CONDITION = 6;
	
	/* First I wrote the displayHangman code and a method, 
	 * testHangman, to test it.
	 * 
	 * Next I wrote the code to play the game, but I set the word to 
	 * be guessed as an unchanging value.
	 * To write this code I started by mostly writing comments
	 * and defining variables I knew I would need later. 
	 * I even called methods without defining them, relying
	 * on the error message to remind me to define the methods later.
	 * For example: I made a call to displayWord before defining that
	 * method.
	 * 
	 * Finally I write code to pull a random word from a dictionary.
	 */
	public static void main(String[] args){
		//I will read in the entire file into a comma separated string
		//named text.
		String text = "";
		//Try-catch statements are mandatory around the file reader
		try{
			//Create a new file reader and pass it the file to read in.
			//I put this file in the project folder next to src and bin.
			//This file contains a huge list of English words, one word
			//per line of text.
			FileReader fr = new FileReader("english.0");
			//Create a new buffered reader for reading in the file.
			BufferedReader bReader = new BufferedReader(fr);
			//Read in each line of the file into the line variable.
			//If line is ever null, that means we have reached the end
			//of the file.
			String line = bReader.readLine();
			while(line != null){
				//Use the indexOf method to check for apostrophes.
				//If the index of the apostrophe equals -1
				//then no apostrophe was found.
				//We use this to filter words with apostrophe's in them.
				if(line.indexOf("'") == -1){
					//Concatenate the latest word with a comma to text.
					text += line+",";
				}
				line = bReader.readLine();
			}
			bReader.close();
		}
		catch(Exception e){
		    //There was a problem!
			System.out.println("ERROR: There was a problem reading the file.\n"+
		    e.getMessage());
			System.exit(1);
		}

		//Split the text on commas into a string array.
		String[] englishWords = text.split(",");
		//Create a random number generator to get a new random string.
		Random rand = new Random();

		//Pick a random number between 0 and one less than the number of words
		//in the array. We go one less because the last word is blank since
		//every word was followed by a comma.
		int randNum = rand.nextInt(englishWords.length-1);
		//This is the word the user will try to guess
		String wordToGuess = englishWords[randNum];
		
		//Create an array with one element for each of the 26 
		//letters in the English alphabet.
		//This will track the letters we have guessed so far.
		String[] lettersGuessed = new String[26];
		//Current index into lettersGuessed
		int lettersIndex = 0;
		
		//Count up the number of mistakes the user has made.
		int mistakes = 0;
		
		//Create a scanner to read in user input
		Scanner in = new Scanner(System.in);
		
		//track whether or not the user has guessed the word.
		boolean youWon = false;

		//Create a temporary variable to store the user's guess.
		CharSequence guess = "";

		/* This is the main loop where the user will make guesses
		 * and we will update the hangman display.
		 */
		while(mistakes < LOSE_CONDITION && !youWon){
			//Print the hangman so far:
			displayHangman(mistakes);
			//Display the word to guess
			displayWord(wordToGuess, lettersGuessed);
			//Display the letters guessed so far.
			//http://stackoverflow.com/questions/409784/simplest-way-to-print-an-array-in-java
			System.out.println("You have guessed:"+Arrays.toString(lettersGuessed));
			//Wait for the user's input
			guess = in.next();
			//Add the user's guess to the list of letters guessed.
			lettersGuessed[lettersIndex] = guess.toString();
			lettersIndex = lettersIndex + 1;
			//Update the number of mistakes.
			if(!wordToGuess.contains(guess)){
				mistakes = mistakes + 1;
				System.out.println("Wrong. The letter "+guess.toString()+" is not in the word.");
			}
			//Check to see if the user won
			youWon = gameWon(wordToGuess, lettersGuessed);
		}

		//Let the user know how the game turned out.
		if(youWon){
			System.out.println("You win! The word is "+wordToGuess);
		}else{
			displayHangman(mistakes);
			System.out.println("You lose! The word is "+wordToGuess);
		}
	}
	
	/* Pre: mistakes is a positive int.
	 * Post: Prints out a hangman and gallows to the command
	 * line based on the number of mistakes the user has made so far.
	 */
	public static void displayHangman(int mistakes){
		String line1 = "  O   |    \n";
		if(mistakes == 0){
			line1 = "      |    \n";
		}
		
		String line2 = "      |    \n";
		if(mistakes >= 4){
			line2 = " \\|/  |    \n";
		}else if(mistakes == 3){
			line2 = " \\|   |    \n";
		}else if(mistakes == 2){
			line2 = "  |   |    \n";
		}
		
		String line3 = "      |    \n";
		if(mistakes >= 5){
			line3 = "  |   |    \n";
		}

		String line4 = "      |    \n";
		if(mistakes >= 6){
			line4 = "  ^   |    \n";
		}

		System.out.println(
				"  -----    \n"+
				"  |   |    \n"+
		line1+//"  O   |    \n"+
		line2+//" \\|/  |    \n"+
		line3+//"  |   |    \n"+
		line4+//"  ^   |    \n"+
				"      |    \n"+
				"  -------- \n");
	}


	/* Pre: wordToGuess is a string. lettersGuessed is a string array.
	 * Post: prints wordToGuess but leaves underscores where the letter
	 * in word to guess is not in the lettersGuessed array.
	 */
	public static void displayWord(String wordToGuess, String[] lettersGuessed){
		System.out.print("Word to Guess: ");
		//Loop over each letter in wordToGuess
		for(int i = 0; i < wordToGuess.length(); i++){
			/* if lettersGuessed contains the character at index i
			 * then print the letter
			 * otherwise print an underscore.
			 */
			char temp = wordToGuess.charAt(i);
			if(stringArrayContains(lettersGuessed, temp)){
				System.out.print(wordToGuess.charAt(i)+" ");
			}else{
				System.out.print("_ ");
			}
		}
		System.out.println("\n");
	}
	
	
	/* Pre: wordToGuess is a string. lettersGuessed is a string array.
	 * Post: Returns true if every letter in wordToGuess is in the 
	 * lettersGuessed array.
	 */
	public static boolean gameWon(String wordToGuess, String[] lettersGuessed){
		//Loop over each letter in wordToGuess
		for(int i = 0; i < wordToGuess.length(); i++){
			/* if lettersGuessed does not contain the character at index i
			 * then return false
			 */
			char temp = wordToGuess.charAt(i);
			if(!stringArrayContains(lettersGuessed, temp)){
				return false;
			}
		}
		return true;
	}
	
	
	/* Pre: strArray is a string array. letter is a character.
	 * Post: returns true if letter is an element of the string array.
	 * returns false otherwise.
	 */
	public static boolean stringArrayContains(String[] strArray, char letter){
		for(int i = 0; i < strArray.length; i++){
			//The char must be converted to a String.
			//http://stackoverflow.com/questions/2429228/in-java-how-does-one-turn-a-string-into-a-char-or-a-char-into-a-string
			if(strArray[i] != null && strArray[i].equalsIgnoreCase(String.valueOf(letter))){
				return true;
			}
		}
		return false;
	}
	

	/* Pre: The method displayHangman exists.
	 * Post: Calls displayHangman with integer arguments 0 through 7 in order.
	 * This is useful to make sure that the displayHangman method works as expected.
	 */
	public static void testHangman(){
		int i = 0;
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
		displayHangman(i++);
	}
}