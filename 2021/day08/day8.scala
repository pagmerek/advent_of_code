import scala.io.Source

object Day8 {
    def first(x: List[(List[String], List[String])]): Int = x match {
       case Nil => 0
       case (_,b)::xs => b.filter(w => List(2,3,4,7) contains w.length).length + first(xs)
    }
    def second(x: List[(List[String], List[String])]): Int = x match {
       case Nil => 0
       case (a,b)::xs => {
           val one   = a.filter(w => w.length == 2).head
           val four  = a.filter(w => w.length == 4).head
           val seven = a.filter(w => w.length == 3).head
           val eight = a.filter(w => w.length == 7).head

           val nine  = a.filter(w => w.length == 6 && four.forall(c => w contains c)).head
           val zero  = a.filter(w => w.length == 6 && w != nine && one.forall(c => w contains c)).head
           val six   = a.filter(w => w.length == 6 && w != nine && w != zero).head

           val three = a.filter(w => w.length == 5 && one.forall(c => w contains c)).head
           val five  = a.filter(w => w.length == 5 && w != three && w.forall(c => nine contains c)).head
           val two   = a.filter(w => w.length == 5 && w != three && w != five).head
           
           val valueMap = Array(("0",zero), ("1", one), ("2",two), ("3",three), ("4",four), ("5", five), ("6",six), ("7", seven), ("8", eight), ("9", nine))
           val decoded = b.map(h => valueMap.filter(p => p._2.sorted == h.sorted)(0)._1).mkString.toInt
           decoded + second(xs)
       }
    }
    def main(args: Array[String]) = {
        val lines = Source.fromFile("input").getLines().toList.map(_.split('|'))
        val input = lines.map(x => (x(0).split(' ').toList.filter(_.!=("")), x(1).split(' ').toList.filter(_.!=(""))))
        println(first(input))
        println(second(input))
    }
}