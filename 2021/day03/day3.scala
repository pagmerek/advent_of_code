import scala.io.Source

object Day3 {
    def calculateFirst(x: List[String]): List[Char] = x match {
            case Nil => Nil
            case x::xs => if (x.filter((h) => h == '1').length > x.length/2) 
                            '1':: calculateFirst(xs) 
                          else 
                            '0':: calculateFirst(xs)
    }
    
    def calculateSecond(lines: List[String], i : Int, c: Char): List[String] = 
            if (lines.length > 1 && i < lines.head.length) {
                val ones = lines.foldLeft(0)((a,b) => if (b(i)=='1') a + 1 else a)
                if (ones >= (lines.length +1)/2) 
                    calculateSecond(lines.filter((x)=> x(i) == c), i+1, c)
                else 
                    calculateSecond(lines.filter((x)=> x(i) != c), i+1, c)
            } 
            else lines 
            
    def first(lines: List[String]): Int = {
            val x = lines.head
            val transposed = (0 until x.length).toList.foldLeft(List[String]())((ta, x) => lines.map((h) => h(x)).mkString :: ta)
            val binary = calculateFirst(transposed)
            val gammaRate = Integer.parseInt(binary.reverse.mkString, 2)
            val epsilonRate = Integer.parseInt(binary.reverse.map((x) => if (x == '0') '1' else '0').mkString, 2)
            epsilonRate * gammaRate
    }
    
    def second(lines: List[String]): Int = {
        val oxygen = Integer.parseInt(calculateSecond(lines,0,'1').head,2)
        val c02 = Integer.parseInt(calculateSecond(lines,0,'0').head,2)
        c02*oxygen
    }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").getLines().toList
        println(first(lines))
        println(second(lines))
    }
}