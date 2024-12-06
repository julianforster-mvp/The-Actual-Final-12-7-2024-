using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class SpeedBoost : MonoBehaviour
{
   public float multiplier = 2f;
   void OnTriggerEnter(Collider other)
   {
       if(other.CompareTag("Player"))
       {
           PickUp(other);
       }
   }
   void PickUp(Collider player)
   {
       PlayerController playerController = player.GetComponent<PlayerController>();

        // Check if the PlayerController component exists
        if (playerController != null)
        {
            // Apply the speed multiplier
            playerController.speed *= multiplier;

            // Output to the console for debugging
            Debug.Log("Power Up Picked Up");

            // Destroy the SpeedBoost object after it has been collected
            Destroy(gameObject);
        }
        else
        {
            Debug.LogWarning("PlayerController not found on " + player.name);
        }
    }
}