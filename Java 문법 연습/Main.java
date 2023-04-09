public class Main {
    public static void main(String[] args){
        final ExternalClass externalClass = new ExternalClass(100,200); 
        //  externalClass = new ExternalClass(); // final로 선언했으므로 재할당 불가능
        String[] strArray = externalClass.returnPuStringArray();
        System.out.println("public int : " + externalClass.puNum);
        System.out.println("private int : " + externalClass.getprivateNum());
        System.out.print("배열 :");
        for(String s: strArray) {
            System.out.print(" " + s);
        }
        System.out.println();
        System.out.println("privateNum : " + externalClass.getprivateNum());
        executePrivateMethodInStaticMethod();
    }
    private static void executePrivateMethodInStaticMethod() {
        System.out.println("private Method execute in static method");
    }
    public static void executeNonStaticPublicMethodInStaticMethod() {
        System.out.println("Non Static Public Method execute in static method");
    }
} 