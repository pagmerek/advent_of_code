import scala.io.Source

object Day6 {
    def first(x: List[Int], days: Int): Int = days match {
        case 0 => x.length
        case n => {
            val births = x.map(_.-(1)).filter(_.==(-1)).length
            val nextEpoch = x.map(a => if (a==(0)) 6 else a-1) ::: List.fill(births)(8)
            first(nextEpoch, days-1)
        }
    }
    def second(x: List[(Int,BigInt)], days: Int): BigInt = days match {
        case 0 => x.foldLeft(BigInt(0))((sum,elem) => sum + elem._2)
        case n => {
            val zero::rest = x
            var nextEpoch = rest.map(a => (a._1-1,a._2)).map(a => if (a._1==6) (a._1,a._2+zero._2) else a) ::: List((8,zero._2))
            second(nextEpoch, days-1)
        }
    }
    def main(args: Array[String]) = {
        val lanterns = Source.fromFile("input").mkString.split(",").map((_.toInt)).toList
        println(first(lanterns,80));
        val countLantern = (0 to 8).map(x => (x, BigInt(lanterns.filter(_.==(x)).length))).toList
        println(second(countLantern, 256))
    }
}