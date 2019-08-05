import java.io.IOException;

import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner teclado = new Scanner(System.in);		
		
		int a = teclado.nextInt();
		int b = teclado.nextInt();
		int soma = a + b ;
		
		System.out.println("X = "+ soma);	

    }
 
}