import scala.io.Source

object Day4 {

    def checkForWinner(board : Array[Array[(Int, Boolean)]]) : Boolean = {
        val winHori = board.map(_.forall(_._2)).exists(_.==(true))       
        val transposedBoard = (0 until board.length).toList.foldLeft(List[Array[(Int, Boolean)]]())((ta, x) => board.map((h) => h(x)) :: ta)
        val winVert = transposedBoard.map(_.forall(_._2)).exists(_.==(true))   
        winHori || winVert                                                                                                                                                                                  
    }

    def first(x: List[Int], boards : List[Array[Array[(Int, Boolean)]]]): Int = x match {
            case Nil => 0
            case x::Nil => 0
            case x::xs => {
                val updated = boards.map(_.map(_.map(a => if (a._1==x) (a._1,true) else (a._1,a._2))))
                val won = updated.filter(a => checkForWinner(a))
                if (won.length > 0) won.head.map(_.filter(_._2.==(false)).map(_._1).sum).sum * x
                else first(xs,updated)
            }
    }
    def second(x: List[Int], boards : List[Array[Array[(Int, Boolean)]]]): Int = x match {
            case Nil => 0
            case x::Nil => 0
            case x::xs => {
                val updated = boards.map(_.map(_.map(a => if (a._1==x) (a._1,true) else (a._1,a._2))))
                val won = updated.filter(a => checkForWinner(a))
                val remove = updated.filter(a => !checkForWinner(a))
                if (remove.length == 0 && won.length == 1) won.head.map(_.filter(_._2.==(false)).map(_._1).sum).sum * x
                else second(xs,remove)
            }
    }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").mkString.split("\n\n").toList
        val values = lines.head.split(",").map(_.toInt).toList
        var boards = lines.tail.map(_.split("\n").map(_.split(" ").filter((x) => x != "").map(x => (x.toInt, false))))
        println(first(values, boards))
        println(second(values, boards))
    }
}