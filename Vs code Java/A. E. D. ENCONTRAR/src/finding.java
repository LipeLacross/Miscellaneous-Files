public class finding {
    public static boolean find(int item, int[] lista)
        {
            for (int i = 0; i < lista.length; i++)
            {
                if (lista[i] == item)
                {
                    return true;
                }
            }
            return false;
        }
}

