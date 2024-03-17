package com.mycompany.hemocromatosisinferencesystem;


import java.util.Scanner;

public class HemocromatosisInferenceSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bienvenido al sistema de inferencia de hemocromatosis.");
        System.out.println("Por favor, responda las siguientes preguntas con 's' para sí y 'n' para no.");

        System.out.println("¿Experimenta dolor en las articulaciones, especialmente en manos y muñecas?");
        char respuestaDolorArticulaciones = scanner.nextLine().charAt(0);

        System.out.println("¿Experimenta fatiga extrema o fatiga crónica?");
        char respuestaFatiga = scanner.nextLine().charAt(0);

        System.out.println("¿Experimenta debilidad muscular y falta de energía?");
        char respuestaDebilidad = scanner.nextLine().charAt(0);

        System.out.println("¿Nota decoloración de la piel, bronceada o grisácea en áreas expuestas al sol?");
        char respuestaDecoloracionPiel = scanner.nextLine().charAt(0);

        System.out.println("¿Ha experimentado pérdida de peso inexplicable?");
        char respuestaPerdidaPeso = scanner.nextLine().charAt(0);

        System.out.println("¿Siente dolor abdominal, especialmente si hay daño en el hígado o el páncreas?");
        char respuestaDolorAbdominal = scanner.nextLine().charAt(0);

        // Lógica de inferencia
        boolean posibleHemocromatosis = (respuestaDolorArticulaciones == 's' || respuestaDolorArticulaciones == 'S')
                && ((respuestaFatiga == 's' || respuestaFatiga == 'S')
                || (respuestaDebilidad == 's' || respuestaDebilidad == 'S')
                || (respuestaDecoloracionPiel == 's' || respuestaDecoloracionPiel == 'S')
                || (respuestaPerdidaPeso == 's' || respuestaPerdidaPeso == 'S')
                || (respuestaDolorAbdominal == 's' || respuestaDolorAbdominal == 'S'));

        if (posibleHemocromatosis) {
            System.out.println("Podría tener hemocromatosis. Le recomendamos buscar atención médica.");
        } else {
            System.out.println("Sus síntomas no parecen indicar hemocromatosis, pero consulte a un médico para un diagnóstico preciso.");
        }

        scanner.close();
    }
}
