import scala.io.Source

object Day1 {
    def first(x: List[Int]): Int = x match {
            case Nil => 0
            case x::Nil => 0
            case x::xs => if (x < xs.head) 1 + first(xs) else first(xs)
    }
    def second(x: List[Int]): Int = x match {
            case Nil => 0
            case x::Nil => 0
            case x::xs => if ((x::xs.take(2)).sum < (xs.take(3)).sum) 1 + second(xs) else second(xs)
        }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("inputdata").getLines().toList.map(_.toInt)
        println(first(lines));
        println(second(lines));

    }
}