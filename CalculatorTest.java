import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {

    @Test
    public void testCalculate() {
        assertEquals(9, Calculator.calculate("4 + 5"));
        assertEquals(15, Calculator.calculate("10 + 5 * 4 - 5"));
        assertEquals(20, Calculator.calculate("10 * 2"));
        assertEquals(0, Calculator.calculate("5 - 5"));
        assertEquals(7, Calculator.calculate("10 - 3 + 1"));
        assertEquals(1, Calculator.calculate("3 - 2"));
        assertEquals(25, Calculator.calculate("5 * 5"));
        assertEquals(2, Calculator.calculate("8 / 4"));
        assertEquals(3, Calculator.calculate("1 + 2 * 1"));
    }
}