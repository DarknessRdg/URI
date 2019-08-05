import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        
        for(int loop = 1; loop <= x; loop ++)
        {
            Josephus lista = new Josephus();
            int qnt = input.nextInt();
            int salto = input.nextInt();
            
            for(int i = 1; i <= qnt; i ++)
                lista.inserir(i);
            
            for(int i = 0; i < qnt - 1; i ++)
                lista.remover(salto);
            
            System.out.println("Case " + loop + ": " + lista.inicio.i);
        }
        
 
    }
 
}

class Josephus {
    No inicio;
    No fim;
    
    public Josephus(){
        inicio = null;
        fim = null;
    }
    
    public void inserir(int i){
        No novo = new No(i);
        if(this.vazio()){
            inicio =  novo;
            fim = inicio;
        }
        else{
            fim.prox = novo;
            fim = novo;
            fim.prox = inicio;
        }
    }
    
    public void remover(int qnt){
        No atual = inicio, anterior = inicio;        
        
        qnt --;
        for(int i = 0; i < qnt; i++){
            if(i == qnt - 1){
                anterior = atual;
            }
            atual = atual.prox;
        }
        if(anterior == atual) // inicio
        {
            inicio = fim;
            fim.prox = atual.prox;
        }
        else{
            anterior.prox = atual.prox;
            inicio = atual.prox;
        }
    }
    
    public void show(){
        System.out.print(inicio.i + " ");
        No aux = inicio.prox;
        while(aux != inicio){
            System.out.print(aux.i + " ");
            aux = aux.prox;
        }
        System.out.println("");
    }
    
    public boolean vazio(){
        return inicio == null;
    }
    
}

class No {
    int i;
    No prox;
    
    public No(int i){
        this.i = i;
        this.prox = null;
    }
}
