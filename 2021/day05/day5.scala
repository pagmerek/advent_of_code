import scala.io.Source

object Day5 {
    def first(values:  List[List[(Int, Int)]], board : Array[Array[Int]]): Int = values match {
            case Nil => { board.map(_.filter(_.>(1)).length).sum }
            case List((a,b), (c,d))::xs  if a == c => {
                val (min, max) = if (b < d) (b,d) else (d,b)
                (min to max).foreach(n => board(a)(n) += 1)
                first(xs, board)
            }
            case List((a,b), (c,d))::xs if b == d => {
                val (min, max) = if (a < c) (a,c) else (c,a)
                (min to max).foreach(n => board(n)(b) += 1)
                first(xs, board)
            }
            case List((a,b), (c,d))::xs => {
                first(xs,board)
            }
    }
    def second(values:  List[List[(Int, Int)]], board : Array[Array[Int]]): Int = values match {
            case Nil => { board.map(_.filter(_.>(1)).length).sum }
            case List((a,b), (c,d))::xs if a == c => {
                val (min, max) = if (b < d) (b,d) else (d,b)
                (min to max).foreach(n => board(a)(n) += 1)
                second(xs, board)
            }
            case List((a,b), (c,d))::xs if b == d => {
                val (min, max) = if (a < c) (a,c) else (c,a)
                (min to max).foreach(n => board(n)(b) += 1)
                second(xs, board)
            }
            case List((a,b), (c,d))::xs => {
                if (a > c && b > d) {
                    val range1 = (a to c by -1)
                    val range2 = (b to d by -1)
                    range1.foreach(x => range2.foreach(y => if (x - y == a - b) board(x)(y)+=1))
                }
                else if (a > c && b < d){
                    val range1 = (a to c by -1)
                    val range2 = (b to d)
                    range1.foreach(x => range2.foreach(y => if (x + y == a + b) board(x)(y)+=1))
                }
                else if (a < c && b > d) {
                    val range1 = (a to c)
                    val range2 = (b to d by -1)
                    range1.foreach(x => range2.foreach(y => if (x + y == a + b) board(x)(y)+=1))
                }
                else if (a < c && b < d) {
                    val range1 = (a to c)
                    val range2 = (b to d)
                    range1.foreach(x => range2.foreach(y => if (x - y == a - b) board(x)(y)+=1))
                }
                second(xs, board)
            }
    }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").getLines().toList
        val values = lines.map(_.split(" -> ").map(x => (x.split(",")(0).toInt, x.split(",")(1).toInt)).toList)
        val board1 = Array.ofDim[Int](1000,1000) 
        val board2 = Array.ofDim[Int](1000,1000) 
        println(first(values, board1))
        println(second(values, board2))
    }
}      