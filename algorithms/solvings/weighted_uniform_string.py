My Java Solution: Track continuous characters and reset the count on character change, use HashSet to improve performance for large strings.

public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int n = in.nextInt();
        char [] charArray = s.toCharArray();
        int contigentString = 1;
        int lastAlphaNum = 0;
        Set<Integer> numList = new HashSet<Integer>();
        for(int i=0 ;i< charArray.length; i ++){
            int alphaNum = charArray[i] -'a'+1;
            if(alphaNum == lastAlphaNum){
                contigentString++;
            }
            else{
                contigentString = 1;
                lastAlphaNum = alphaNum;
            }
            int num = (alphaNum) * contigentString;
            numList.add(num);
        }
        for(int a0 = 0; a0 < n; a0++){
            int x = in.nextInt();
            if(numList.contains(x) ){
                System.out.println("Yes");
            }
            else{
                System.out.println("No");
            }
        }
    }
