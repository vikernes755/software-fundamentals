// import static org.junit.jupiter.api.Assertions.assertEquals;

// import org.junit.jupiter.api.Test;

public class Main {
  public static void main(String[] args) {
    //1. define vars and/ord const
    float n1, n2, add, sub, multi, div;

    //2.initialize vars and/or const
    
    n1 = 10;
    n2 = 3;
//3. procesess
    add = n1 + n2;
    sub = n1 - n2;
    multi = n1 * n2;
    div = n1 / n2;


    //outputs

    System.out.printf("addition: " +  add);
    System.out.printf("subtraction: " + sub);
    System.out.printf("multiplication: " + multi);
    System.out.printf("division: " + div);





System.out.printf("#######################");
System.out.printf("p and q");
System.out.printf("#######################");

System.out.printf("V	^	V :" +  (true && true));
System.out.printf("V	^	F :" +  (true && false));
System.out.printf("F	^	V :" +  (false && true));
System.out.printf("F	^	F:" +  (false && false));


System.out.printf("#######################");
System.out.printf("p or q");
System.out.printf("#######################");

System.out.printf("V	v	V :" +  (true || true));
System.out.printf("V	v	F :" +  (true || false));
System.out.printf("F	v	V :" +  (false || true));
System.out.printf("F	v	F:" +  (false || false));


System.out.printf("#######################");
System.out.printf(((object)3.14).getClass().getName());// ---> print(type(3.14))


float y = 13.14151455445f;
System.out.print(y);

//conclusion:
//elnumero 3.14 es DOUBLE  por defecto
//el numero 3.14f es FLOAT


    
  }

  // @Test
  // void addition() {
  //     assertEquals(2, 1 + 1);
  // }
}