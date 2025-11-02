# PowerShell script to add READMEs to all GitHub repositories
# This script will clone each repo, add the README, and push it back

$repos = @(
    @{Name='githubemc1'; Readme='README_githubemc1.md'},
    @{Name='githubemc2'; Readme='README_githubemc2.md'},
    @{Name='HeroHomeemc'; Readme='README_HeroHomeemc.md'},
    @{Name='JFALuckyPalace'; Readme='README_JFALuckyPalace.md'},
    @{Name='mcp-learning-path-demo'; Readme='README_mcp-learning-path-demo.md'},
    @{Name='password-manager'; Readme='README_password-manager.md'},
    @{Name='rajalakshmiwebsite'; Readme='README_rajalakshmiwebsite.md'},
    @{Name='securityvalut'; Readme='README_securityvalut.md'}
)

$tempDir = "C:\Users\user\Desktop\temp_readme_update"
$sourceDir = "C:\Users\user\Desktop\pet_chatbot"

Write-Host "Starting README update process..." -ForegroundColor Green

# Create temp directory
if (Test-Path $tempDir) {
    Remove-Item $tempDir -Recurse -Force
}
New-Item -ItemType Directory -Path $tempDir | Out-Null

foreach ($repo in $repos) {
    $repoName = $repo.Name
    $readmeFile = $repo.Readme
    $repoPath = Join-Path $tempDir $repoName
    
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "Processing: $repoName" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    
    try {
        # Clone repository
        Write-Host "Cloning repository..." -ForegroundColor Gray
        git clone "https://github.com/Ajaykannagit/$repoName.git" $repoPath 2>&1 | Out-Null
        
        if (Test-Path $repoPath) {
            # Copy README file
            $sourceReadme = Join-Path $sourceDir $readmeFile
            $targetReadme = Join-Path $repoPath "README.md"
            
            if (Test-Path $sourceReadme) {
                Copy-Item $sourceReadme $targetReadme -Force
                Write-Host "README copied successfully" -ForegroundColor Green
                
                # Navigate to repo and commit
                Set-Location $repoPath
                
                # Check if README already exists and is different
                $hasChanges = git diff --quiet README.md
                if (-not $hasChanges) {
                    Write-Host "No changes detected (README already exists and is same)" -ForegroundColor Yellow
                } else {
                    git add README.md
                    git commit -m "Add professional README file" 2>&1 | Out-Null
                    Write-Host "Changes committed locally" -ForegroundColor Green
                    
                    # Push to GitHub
                    Write-Host "Pushing to GitHub..." -ForegroundColor Gray
                    git push origin main 2>&1 | Out-Null
                    Write-Host "Pushed successfully!" -ForegroundColor Green
                }
                
                Set-Location $sourceDir
            } else {
                Write-Host "Source README file not found: $sourceReadme" -ForegroundColor Red
            }
        }
    } catch {
        Write-Host "Error processing $repoName : $_" -ForegroundColor Red
    }
    
    # Cleanup
    if (Test-Path $repoPath) {
        Remove-Item $repoPath -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "All repositories processed!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nCheck your GitHub repositories to see the updated READMEs." -ForegroundColor Yellow

# Cleanup temp directory
if (Test-Path $tempDir) {
    Remove-Item $tempDir -Recurse -Force -ErrorAction SilentlyContinue
}

