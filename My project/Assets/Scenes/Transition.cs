using UnityEngine;
using UnityEngine.Playables; // For Timeline
using UnityEngine.SceneManagement; // For scene loading
using System.Collections; // For IEnumerator

public class CutsceneController : MonoBehaviour
{
    public PlayableDirector cutsceneDirector;  // Reference to the PlayableDirector (Timeline)
    public string nextSceneName = "GameScene"; // The scene you want to transition to

    void Start()
    {
        // Start the cutscene immediately when the scene starts
        StartCutscene();
    }

    public void StartCutscene()
    {
        // Play the cutscene Timeline
        if (cutsceneDirector != null)
        {
            cutsceneDirector.Play();
            // Listen for the end of the cutscene
            cutsceneDirector.stopped += OnCutsceneFinished;
        }
    }

    // This function will be called when the cutscene finishes
    private void OnCutsceneFinished(PlayableDirector director)
    {
        // Optionally, you can add a delay before transitioning to the game
        // You could use a coroutine to add a delay
        StartCoroutine(TransitionToGame());
    }

    // Transition to the game scene (could be the next level or the gameplay scene)
    private IEnumerator TransitionToGame()
    {
        // Add a small delay if needed for a smoother transition
        yield return new WaitForSeconds(1f);

        // Load the game scene
        SceneManager.LoadScene("SampleScene");
    }
}