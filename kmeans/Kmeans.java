import java.util.*;
import java.io.*;

public class Kmeans{
	public static void main(String args[]){
		ArrayList<Integer> C1 = new ArrayList<>();
		ArrayList<Integer> C2 = new ArrayList<>();
		float d1=0,d2=0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		System.out.println("Enter the Data Elements Seperated by a comma ");
		try{
			String ip = br.readLine();
			String temp[] =ip.trim().split(",");
			int elements[] = new int[temp.length];
			for(int i=0;i<temp.length;i++){
				elements[i]= Integer.parseInt(temp[i]);
			}

			float p,q;
			System.out.println("Select a cluster point p : ");
			p=Integer.parseInt(br.readLine());
			System.out.println("Select a cluster point q : ");
			q=Integer.parseInt(br.readLine());
			boolean flag = false;
			while(flag!=true){
				
				float mean1=0,mean2=0;
				for(int e : elements){
					d1=Math.abs(e-p);
					d2=Math.abs(e-q);
					if(d1<=d2){
						C1.add(e);
						mean1=mean1+e;
					}else{
						C2.add(e);
						mean2=mean2+e;
					}
				}
				System.out.println("------------------------------------------\nP = "+p);
				System.out.println("Cluster C1 = "+C1);
				System.out.println("Q = "+q);
				System.out.println("Cluster C2 = "+C2);

				mean1=mean1/C1.size();
				mean2=mean2/C2.size();

				if(mean1==p && mean2==q){
					flag = true;
				}
				else{

				 	p=mean1;
				 	q=mean2;
				 	C1.clear();
				 	C2.clear();
				 }	 	
			}
		}catch(IOException e){
			System.out.println("Caugth IOException");
		}
		
	}
}