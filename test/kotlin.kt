import kotlin.math.sqrt

data class Person(val name: String, val age: Int)

fun main() {
    val number = 16.0
    val result = sqrt(number)
    println("Square root of $number is $result")

    val people = listOf(Person("Alice", 30), Person("Bob", 25))
    for (person in people) {
        println("${person.name} is ${person.age} years old")
    }
}
