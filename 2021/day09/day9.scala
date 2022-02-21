import scala.io.Source

object Day9 {
    def findLowPoints(x: Array[Array[Int]]) : List[(Int,Int)] = {
        (1 until x.length - 1).map(i => {
            (1 until x(i).length - 1).map(j =>{
                if (x(i)(j) < x(i+1)(j) && x(i)(j) < x(i-1)(j) && x(i)(j) < x(i)(j+1) && x(i)(j) < x(i)(j-1))
                    (i,j)
                else
                    (-1,-1)
            }).filter(_.!=((-1,-1))).toList
        }).toList.flatten
    }

    def getBasinSize(pos: (Int,Int), x: Array[Array[(Int,Boolean)]]) : Int = x(pos._1)(pos._2) match {
        case (9,_) => 0
        case (_, true) => 0
        case (_,_) => {
            x(pos._1)(pos._2) = (x(pos._1)(pos._2)._1, true)
            1 + getBasinSize((pos._1 - 1, pos._2),x) + getBasinSize((pos._1 + 1, pos._2),x) + getBasinSize((pos._1, pos._2 - 1),x) + getBasinSize((pos._1, pos._2 + 1),x)
        }
    }

    def first(x: Array[Array[Int]]): Int = {
       findLowPoints(x).map(h => x(h._1)(h._2) + 1).sum
    }
    def second(x: Array[Array[Int]]): Int = {
        val visitedX = x.map(_.map(a => (a, false)))
        findLowPoints(x).map(p => getBasinSize(p,visitedX)).sorted.reverse.take(3).product
    }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").getLines().toArray.map(x => x.toCharArray().map(y => y.toInt - 48).toArray)
        val wall = (0 until lines.head.length +2).map(x=>9).toArray
        val modified = Array(wall) ++ lines.map(x =>  Array(9) ++ x ++ Array(9)) ++ Array(wall)
        println(first(modified))
        println(second(modified))
    }
}