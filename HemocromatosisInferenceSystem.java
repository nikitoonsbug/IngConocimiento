package com.mycompany.hemocromatosisinferencesystem;
import java.util.Scanner;

public class HemocromatosisInferenceSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bienvenido al sistema de inferencia de hemocromatosis.");
        System.out.println("Por favor, responda las siguientes preguntas con 's' para sí y 'n' para no.");

        int totalPreguntas = 14; // Número total de preguntas
        int respuestasPositivas = 0; // Inicializar contador de respuestas positivas

        // Preguntar al usuario y contar respuestas afirmativas
        System.out.println("¿Experimenta dolor en las articulaciones, especialmente en manos y muñecas?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0)) * 2; // Pregunta con más peso

        System.out.println("¿Experimenta fatiga extrema o fatiga crónica?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Experimenta debilidad muscular y falta de energía?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Nota decoloración de la piel, bronceada o grisácea en áreas expuestas al sol?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha experimentado pérdida de peso inexplicable?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Siente dolor abdominal, especialmente si hay daño en el hígado o el páncreas?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha experimentado cambios en la pigmentación de la piel, como manchas oscuras o áreas hiperpigmentadas?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha notado cambios en el color de sus deposiciones, como heces de color oscuro o alquitranadas?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Experimenta problemas de salud relacionados con la función hepática, como hepatitis o cirrosis?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha tenido problemas cardíacos, como palpitaciones o dificultad para respirar?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha sido diagnosticado previamente con diabetes o hipotiroidismo?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Tiene antecedentes familiares de hemocromatosis u otros trastornos genéticos relacionados con el metabolismo del hierro?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        System.out.println("¿Ha experimentado cambios en el funcionamiento sexual o reproductivo?");
        respuestasPositivas += obtenerRespuestaPositiva(scanner.nextLine().charAt(0));

        // Calcular el porcentaje de respuestas afirmativas
        double porcentajeRespuestasPositivas = ((double) respuestasPositivas / (totalPreguntas)) * 100; // Multiplicar total de preguntas por 2

        // Mostrar resultados
        System.out.println("Porcentaje de respuestas afirmativas: " + porcentajeRespuestasPositivas + "%");

        // Lógica de inferencia
        boolean posibleHemocromatosis = porcentajeRespuestasPositivas >= 50;

        if (posibleHemocromatosis) {
            System.out.println("Podría tener hemocromatosis. Le recomendamos buscar atención médica.");
        } else {
            System.out.println("Sus síntomas no parecen indicar hemocromatosis, pero consulte a un médico para un diagnóstico preciso.");
        }

        scanner.close();
    }

    // Método para obtener el valor de respuesta positiva
    public static int obtenerRespuestaPositiva(char respuesta) {
        return (respuesta == 's' || respuesta == 'S') ? 1 : 0;
    }
}

