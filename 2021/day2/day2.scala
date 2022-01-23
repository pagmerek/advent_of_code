import scala.io.Source

object Day2 {
    def first(x: List[(String,Int)]): (Int, Int) = x match {
            case Nil => (0,0)
            case ("forward", x)::xs => {
                val y = first(xs)
                (y._1 + x, y._2)
            }
            case ("down", x)::xs => {
                val y = first(xs)
                (y._1 , y._2 + x)
            }
            case ("up", x)::xs => {
                val y = first(xs)
                (y._1, y._2 - x)
            }
    }
    def second(x: List[(String,Int)]): (Int, Int, Int) = x match {
            case Nil => (0,0,0)
            case ("forward", x)::xs => {
                val y = second(xs)
                (y._1 + x, y._2 + (y._3 * x), y._3)
            }
            case ("down", x)::xs => {
                val y = second(xs)
                (y._1 , y._2, y._3 + x)
            }
            case ("up", x)::xs => {
                val y = second(xs)
                (y._1, y._2, y._3 - x)
            }

        }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").getLines().toList
        val commands = lines.map((x) => x.split(" ")).map {case Array(f1,f2) => (f1, f2.toInt)}
        
        val firstResult = first(commands)
        println(firstResult._1 * firstResult._2)
        val secondResult = second(commands.reverse)
        println(secondResult._1 * secondResult._2)

    }
}