import scala.io.Source

object Day7 {
    def first(x: List[Int]): Int = {
        val med = x.sorted.drop(x.length/2).head
        x.foldLeft(0)((acc, n) => (n - med).abs + acc)
    }
    def second(x: List[Int]): Int = {
       val mean = x.sum/x.length
       x.foldLeft(0)((acc, n) => ((n - mean).abs +1)*(n - mean).abs/2 + acc)
    }
    def main(args: Array[String]) = {
        val crabs = Source.fromFile("input").mkString.split(",").map((_.toInt)).toList
        println(first(crabs))
        println(second(crabs))
    }
}